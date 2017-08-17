//REQUIRE haroboardUtility.js

var DashboardManager = (function () {
    "use strict";

    var registeredProjects = null;
    var logoList = null;


    var projectData = {
        pages : [],
        logo : ""

    };

    function fetchAllRegisteredProjects() {
        var httpClient = haroboardUtility.httpClient;
        httpClient.get('/registeredprojects', null, function (response) {
            registeredProjects = JSON.parse(response.responseText);
        });
    }

    function fetchAllRegisteredLogos() {
        var httpClient = haroboardUtility.httpClient;
        httpClient.synchronized_get("/get_icons", null, function (response) {
            logoList = JSON.parse(response.responseText);
        });
    }

    fetchAllRegisteredProjects();
    fetchAllRegisteredLogos();

    function getRegisteredProjects() {
        return registeredProjects;
    }

    function doesSiteAlreadyExist(siteName) {
        var doesExist = false;
        for (var i in registeredProjects) {
            if (registeredProjects[i].toLowerCase() === siteName.toLowerCase()) {
                doesExist = true;
                break;
            }
        }
        return doesExist;
    }

    function addPage(pageName, pageType, logo) {
        var page = new Page(pageName, pageType);
        if(logo !== null && logo !== "undefined") {
            page.addLogo(logo);
        }
        projectData.pages.push(page);
    }

    function getRegisteredLogos() {
        return logoList;
    }

    return {
        getRegisteredProjects: getRegisteredProjects,
        doesSiteAlreadyExist: doesSiteAlreadyExist,
        getAllRegisteredLogos : getRegisteredLogos
    };

})();