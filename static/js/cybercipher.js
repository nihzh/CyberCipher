$(document).ready(function() {
    refreshHistory();
    const inactivityTime = 5 * 60 * 1000;  // inactivity time for clearing session, in ms
    let timeout;

    // navigation switching
    $('.nav-link').click(function(e) {
        e.preventDefault();
        $('.nav-link').removeClass('active');
        $(this).addClass('active');
        $('.cipher-card').hide();
        $('#' + $(this).data('target')).show();
        $("#navbarNav").collapse("hide");
    });

    // copy button
    $('#main-area').on("click", ".copy-btn", function() {
        const textElement = $(this).prev('input, textarea');
        navigator.clipboard.writeText(textElement.val());
        toastr.info("Result copied", "Info");
    });

    // clear history button
    $('#clear-history').click(function(){
        clearSession();
    });

    // affine cipher: encrpt/decrypt button action
    $('#aff-encrypt, #aff-decrypt').click(function() {
        // locate to affine cipher card
        const card = $(this).closest('.cipher-card');
        
        // encrypt or decrypt
        const actionType = $(this).attr('id') == "aff-encrypt" ? 'enc':'dec';

        // input values
        const inputText = card.find('#originArea').val();
        const keyA = parseInt(card.find('#key-a').val());
        const keyB = parseInt(card.find('#key-b').val());

        if(inputText.length == 0){
            toastr.warning("Write something as origin text 0.o", "Alert");
            return false;
        }

        const INVERSE = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25];
        // keys validation
        // keya: is number and included in INVERSE list (relatively prime with 26)
        if(isNaN(keyA) || !isFinite(keyA) || !INVERSE.includes(keyA)){
            toastr.warning("Please select a key A!", "Alert");
            return false;
        }
        // keyb: number
        if(isNaN(keyB) || !isFinite(keyB)){
            toastr.warning("Please input key B with a number!", "Alert");
            return false;
        }

        sendRequest2Keys(inputText, keyA, keyB, "affine", actionType, card);
    });

    // shift cipher: encrpt/decrypt button action
    $('#sft-encrypt, #sft-decrypt').click(function() {
        // locate to affine cipher card
        const card = $(this).closest('.cipher-card');
        
        // encrypt or decrypt
        const actionType = $(this).attr('id') == "sft-encrypt" ? 'enc':'dec';

        // input values
        const inputText = card.find('#originArea').val();
        let keyA = card.find('#key-a').val();

        if(inputText.length == 0){
            toastr.warning("Write something as origin text o.0", "Alert");
            return false;
        }

        // letter or number between 0-25
        if(!isNaN(parseInt(keyA)) && isFinite(parseInt(keyA))){
            keyA = parseInt(keyA);
        }
        // is a pure letter
        else if(/^[A-Za-z]{1}$/.test(keyA) && keyA.length == 1){
            // 97: lower a in ascii
            keyA = keyA.toLowerCase().charCodeAt(0) - 97;
        }
        else{
            toastr.warning("The key must be one number or one letter!", "Alert");
            return false;
        }

        sendRequest2Keys(inputText, keyA, null, "shift", actionType, card);
    });

    // vigenere cipher: encrpt/decrypt button action
    $('#vig-encrypt, #vig-decrypt').click(function() {
        // locate to affine cipher card
        const card = $(this).closest('.cipher-card');
        
        // encrypt or decrypt
        const actionType = $(this).attr('id') == "vig-encrypt" ? 'enc':'dec';

        // input values
        const inputText = card.find('#originArea').val();
        const keyA = card.find('#key-a').val();

        if(inputText.length == 0){
            toastr.warning("Write something as origin text o.0", "Alert");
            return false;
        }

        // The key must be pure letters
        if(!/^[A-Za-z]+$/.test(keyA)){
            toastr.warning("The key must be pure alphabet letters", "Alert");
            return false;
        }

        sendRequest2Keys(inputText, keyA, null, "vigenere", actionType, card);
    });

    // random key encryption
    $("[id*='rdmkey']").click(function() {
        const card = $(this).closest('.cipher-card');
        const cipherType = card.attr('id');
        const inputText = card.find('#originArea').val();

        if(inputText.length == 0){
            toastr.warning("Write something as origin text o.0", "Alert");
            return false;
        }
        sendRequest0Key(inputText, cipherType, "rdmenc", card);
    });

    $("[id*='analysis']").click(function() {
        const card = $(this).closest('.cipher-card');
        const cipherType = card.attr('id');
        const inputText = card.find('#originArea').val();

        if(inputText.length == 0){
            toastr.warning("Write something as origin text o.0", "Alert");
            return false;
        }
        sendRequest0Key(inputText, cipherType, "anldec", card);
    });


    function sendRequest2Keys(originText, keyA, keyB, cipherType, actionType, card){
        const csrfToken = $('meta[name="csrf-token"]').attr('content')
        $.ajax({
            url: "/" + cipherType + "/" + actionType,
            type: "POST",
            contentType: "application/json",
            headers: {
                'X-CSRFToken': csrfToken
            },
            data: JSON.stringify({text: originText, keyA: keyA, keyB: keyB}),
            success: function (response) {
                resultText = response.result;
                if(response.result != null){
                    card.find('#resultArea').val(response.result);  
                }
                console.log(keyA)
                addHistory(originText, keyA, keyB, resultText, actionType, cipherType, moment().format("YYYY-MM-DD HH:mm:ss"))
                toastr.success("Action Successed", "Success");
            },
            error: function() {
                toastr.error("Network Error!", "Error");
            }
        })
    }

    function sendRequest0Key(originText, cipherType, actionType, card){
        const csrfToken = $('meta[name="csrf-token"]').attr('content')
        $.ajax({
            url: "/" + cipherType + "/" + actionType,
            type: "POST",
            contentType: "application/json",
            headers: {
                'X-CSRFToken': csrfToken
            },
            data: JSON.stringify({text: originText}),
            success: function (response) {
                resultText = response.result;
                keyA = response.keyA || null;
                keyB = response.keyB || null;

                if(response.result.length == 0){
                    card.find('#resultArea').val("**Failed, the text may not long enough for analysis.**");
                }
                else{
                    card.find('#resultArea').val(response.result);
                }
                // display the key when random encrypt
                if(response.keyA != null){
                    card.find('#key-a').val(response.keyA);
                }
                if (card.attr("id") == "affine" && response.keyB != null){
                    card.find('#key-b').val(response.keyB);
                }
                addHistory(originText, keyA, keyB, resultText, actionType, cipherType, moment().format("YYYY-MM-DD HH:mm:ss"))
                toastr.success("Action Successed", "Success")
            },
            error: function() {
                toastr.error("Network Error!", "Error");
            },
            falure: function(){
                toastr.error("Illegal Input!", "Error");
            }
        })
    }

    function addHistory(originText, keyA, keyB, resultText, actionType, cipherType, timestamp){
        // get history list from session
        let history = JSON.parse(sessionStorage.getItem("cipherHistory")) || [];
        // create new history record
        let newRecord = {
            originText: originText,
            resultText: resultText,
            keyA: keyA,
            keyB: keyB ?? "",
            actionType: actionType,
            cipherType: cipherType,
            timestamp: timestamp || moment().format("YYYY-MM-DD HH:mm:ss")
        };
        // add record into list
        history.push(newRecord);
        // put into session, reset session timer
        sessionStorage.setItem("cipherHistory", JSON.stringify(history));
        resetTimer()
        // refresh list
        refreshHistory();
    }

    function refreshHistory(){
        let container = $("#historyList");
        let history = JSON.parse(sessionStorage.getItem("cipherHistory")) || [];

        if (history.length == 0){
            container.html("<p class='mx-3 text-secondary'>Currently Empty</p>");
            return;
        }

        let htmlLists = "";
        // display from the end of list (newest record)
        history.slice().reverse().forEach((record) => {
            actionType = "";
            switch (record.actionType){
                case "enc":
                    actionType = "Encrypt";
                    break;
                case "dec":
                    actionType = "Decrypt";
                    break;
                case "rdmenc":
                    actionType = "Random Encrypt";
                    break;
                case "anldec":
                    actionType = "Cryptanalysis";
                    break;
                default:
                    actionType = "actionType";
                    break;
            }
            cipherType = "";
            switch (record.cipherType){
                case "affine":
                    cipherType = "Affine";
                    break;
                case "shift":
                    cipherType = "Shift";
                    break;
                case "vigenere":
                    cipherType = "Vigenère";
                    break;
                default:
                    cipherType = "cipherType";
                    break;
            }
            htmlLists += `
            <div class="history-item container mt-3">
                <div class="row mx-1">
                    <div class="col-6">
                        <b class="text-left">${cipherType} - ${actionType}</b>
                    </div>
                    <div class="col-6 text-end">
                        <small class="text-muted">${record.timestamp}</small>
                    </div>
                </div>
            
                <div class="d-flex justify-content-center">
                    <div class="row mx-1 mt-1">
                        <div class="col-md-4">
                            <div class="form-group">
                                <label for="history-origin-text" class="ms-1"><small>Origin Text</small></label>
                                <div class="copy-container">
                                    <textarea id="history-origin-text" class="form-control history-form" rows="4" readonly>${record.originText}</textarea>
                                    <button class="btn btn-secondary btn-light copy-btn history-copy-btn-bottom">Copy</button>
                                </div>
                                
                            </div>
                        </div>
        
                        <div class="col-md-4">
                            <div class="form-group">
                                <label for="history-key-a" class="ms-1"><small>Key A</small></label>
                                <div class="copy-container">
                                    <input type="text" id="history-key-a" class="form-control history-input" value="${record.keyA}" readonly>
                                    <button class="btn btn-secondary btn-light copy-btn history-copy-btn-right">
                                        <i class="bi bi-clipboard"></i>
                                    </button>
                                </div>
                                
                            </div>
                            <div class="form-group mt-2">
                                <label for="history-key-b" class="ms-1"><small>Key B</small></label>
                                <div class="copy-container">
                                    <input type="text" id="history-key-b" class="form-control history-input" value="${record.keyB}" readonly>
                                    <button class="btn btn-secondary btn-light copy-btn history-copy-btn-right">
                                        <i class="bi bi-clipboard"></i>
                                    </button>
                                </div>
                            </div>
                        </div>
        
                        <div class="col-md-4">
                            <div class="form-group">
                                <label for="history-result-text" class="ms-1"><small>Result Text</small></label>
                                <div class="copy-container">
                                    <textarea id="history-result-text" class="form-control history-form" rows="4" readonly>${record.resultText}</textarea>
                                    <button class="btn btn-secondary btn-light copy-btn history-copy-btn-bottom">Copy</button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            `;
        });
        container.html(htmlLists);
    }

    function clearSession(){
        sessionStorage.clear();
        refreshHistory();
        toastr.info("Record cleared", "History");
    }

    function resetTimer() {
        clearTimeout(timeout);
        timeout = setTimeout(clearSession, inactivityTime);
    }
});