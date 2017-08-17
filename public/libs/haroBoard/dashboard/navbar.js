//This class implements the navbar and generates the code required for the navbar.

function Navbar() {
    this.alignement = Navbar.Alignment.LEFT;
    this.logo = null;
    this.isLogoCentered = false;
    this.brandLink = null;
    this.shouldShowActiveLink = true;
    this.isExtendedWithTabs = false;
    this.tabs = [];
    this.isFixed = false;
    this.components = [];
}

Navbar.prototype.AddComponent = function (component) {
    //TODO: Add some validation
    this.components.push(component);
};

Navbar.prototype.SetAlignment = function (alignment) {
    if (typeof alignment === Navbar.Alignment) {
        this.alignement = alignment;
    }
};


Navbar.Alignment = {
    LEFT: "left",
    RIGHT: "right",
    CENTER: "center"
};

Navbar.DropdownTypes = {
    LINK: "link",
    DIVIDER: "divider"
};

//TODO: Add translated fields in the configuration
Navbar.ComponentTypes = {
    LINK: "link",
    DROPDOWN: "Dropdown",
    ICON_LINK: "icon-link",
    BUTTON: "button",
    SEARCH_BAR: "search_bar"
};