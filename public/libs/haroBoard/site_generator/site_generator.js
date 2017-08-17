var siteGenerator = function () {
    "use strict"

    //__GLOBAL_VARIABLES_
    var isCompleted = false;
    var currentlySelectedSite = {};
    var allSites = [];
    //___END_GLOBAL_VARIABLES_

    function init() {
        queue()
            .defer(d3.json, "/lochistorydata")
            .await(makeGraphs);

    }


    function findAllSites() {
        var retval = [];
        //Scan file directory, recursivly down, but nothing up


        return retval;
    }

}();