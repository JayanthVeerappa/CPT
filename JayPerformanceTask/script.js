document.getElementById("actionButton").addEventListener("click", function() {
    let content = document.querySelector(".content");
    content.style.transform = "scale(1.1)";
    setTimeout(() => content.style.transform = "scale(1)", 200);
});
