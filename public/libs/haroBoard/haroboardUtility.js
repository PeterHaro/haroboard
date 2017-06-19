var haroboardUtility = function () {
    "use strict";

    var httpClient = function () {
        this.getRequest = function (url, callback) {
            var xmlHttpRequest = new XMLHttpRequest();
            xmlHttpRequest.onreadystatechange = function () {
                if (xmlHttpRequest.readyState === 4 && xmlHttpRequest.status === 200) {
                    callback(xmlHttpRequest.responseText);
                }
            };
            xmlHttpRequest.open("GET", url, true);
            xmlHttpRequest.send();
        }
    };

    return {
        httpClient: httpClient
    };

}();