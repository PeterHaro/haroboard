/*    LINK: "link",
    LINK_WITH_ICON: "LinkWithIcon",
    DROPDOWN: "Dropdown",
    ICON_LINK: "icon-link",
    BUTTON: "button",
    SEARCH_BAR: "search_bar"
    */

function ListItemLink(name) {
    this.href = "#!";
    this.name = name;
}

var ButtonTypes = {
    LARGE : "btn-large",
    NORMAL : "btn",
    FLAT : "btn-flat",
    FLOATING : "btn-floating"
};

function Button(text, buttonType) {
    this.isDisabled = false;
    this.text = text;
    this.buttonType = buttonType;
    this.logo;
}

function ListItemWithLink(name) {
    this.href = "#!";
    this.name = name;
    this.logo = "none-selected";
    this.linkDirection = "none-selected";
}

function NavbarDropdownMenu() {
    self.items = [];
}

NavbarDropdownMenu.prototype.AddItem = function (item) {
    self.items.push(item);
};

function NavbarDropdownMenuItem(name) {
    this.href = "#!";
    this.name = name;
}

function NavbarDropdownMenuDivider() {
    this.divider = "divider";
}