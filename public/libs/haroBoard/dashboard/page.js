function Page(name, type) {
    this.name = name;
    this.type = type;

    this.addLogo = function(logo) {
        this.logo = logo;
    }
}