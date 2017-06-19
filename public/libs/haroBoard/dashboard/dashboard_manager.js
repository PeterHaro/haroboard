var DashboardManager = (function () {
    "use strict";

    var registeredProjects = null;



    function fetchAllRegisteredProjects() {
        var httpClient = haroboardUtility.httpClient();
        httpClient.get('/registeredprojects', function(response) {
            registeredProjects = response.responseText;
        });
    }

    fetchAllRegisteredProjects();

    function getRegisteredProjects() {
        return registeredProjects;
    }

    function startDashboardManagerTour() {

    }

    return {
        getRegisteredProjects : getRegisteredProjects
    };

})();