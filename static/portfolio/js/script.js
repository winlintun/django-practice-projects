// Fixing Flexbox gap property missing in some Safari version

function checkFlexGap() {
    var flex = document.createElement("div");
    flex.style.display = "flex";
    flex.style.flexDirection ="column";
    flex.style.rowGap = "1px";

    flex.appendChild(document.createElement("div"));
    flex.appendChild(document.createElement("div"));

    document.body.appendChild(flex);

    var isSupported = flex.scrollHeight === 1;
    flex.parentNode.removeChild(flex);
    console.log(isSupported);

    if (!isSupported) document.body.classList.add("no-flexbox-gap");
}

checkFlexGap();

// Sticky Navigation

const sectionHeroEL = document.querySelector(".section-hero");
const obs = new IntersectionObserver(
    function (enteries) {
        const ent = enteries[0];
        console.log(ent);
        if (ent.isIntersecting === false) {
            document.body.classList.add("sticky");
        }
        if (ent.isIntersecting === true) {
            document.body.classList.remove("sticky");
        }
    },
    {
        // In the view port
        root: null,
        threshold: 0,
        rootMargin: "-80px",
    }
);

obs.observe(sectionHeroEL);

// Scroll Animation
const allLinks = document.querySelectorAll("a:link");

allLinks.forEach(function(link){
    link.addEventListener("click", function(e) {
        e.preventDefault();
        const herf = link.getAttribute("href");
        if(herf === "#"){
            window.scrollTo({
                top: 0,
                behavior: "smooth",
            });
        }
        if(herf !== "#" && herf.startsWith("#")) {
            const selectEL = document.querySelector(herf);
            selectEL.scrollIntoView({
                behavior: "smooth",
            })
        }
    });
});
