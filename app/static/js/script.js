const headerDropImg = document.getElementById("headerDropImg");
const headerDropMenu = document.getElementById("headerDropMenu");

headerDropImg.addEventListener("click", () => {
    headerDropMenu.classList.toggle("go-down");
    headerDropMenu.classList.toggle("go-up");
})

// headerDropImg.addEventListener("mouseenter", () => {
//     headerDropMenu.style.animation= "dropdown-menu 1s forwards";
// })

// headerDropImg.addEventListener("mouseleave", () => {
//     headerDropMenu.style.animation= "moveBackwards 1s forwards";
// })

console.log(headerDropImg);
