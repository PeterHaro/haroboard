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
    this.logo = null;
}

function ListItemIcon() {
    this.logo ="none-selected";
    this.alignment = "left";
}

function ListItemWithLink() {
    this.type = Navbar.ComponentTypes.LINK;
    this.itemName = "";
    this.href = "#!";
    this.name = "";
    this.logo = new ListItemIcon();
    this.linkDirection = "none-selected";
}

ListItemWithLink.prototype.addLogo = function(name, alignment) {
    if(name !== null && typeof(name) === "string" && name.trim() !== "") {
        this.logo.logo = name;
        this.logo.alignment = alignment;
    } else {
        this.logo = "none-selected";
    }
};

ListItemWithLink.prototype.addItemName = function(name) {
  if(name !== null && typeof(name) === "string" && name.trim() !== "") {
        this.itemName = name;
        return true;
    }
    return false;
};

ListItemWithLink.prototype.addName = function (name) {
    if(name !== null && typeof(name) === "string" && name.trim() !== "") {
        this.name = name;
        return true;
    }
    return false;
};

ListItemWithLink.prototype.getId = function() {
    return this.itemName;
};

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