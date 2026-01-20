// Navbar piilottaminen hero-kuvan kohdalla
document.addEventListener("scroll", () => {
    const navbar = document.getElementById("navbar");
    if (window.scrollY > window.innerHeight * 0.7) {
        navbar.classList.add("bg-dark");
    } else {
        navbar.classList.remove("bg-dark");
    }
});

