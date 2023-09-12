const form = document.querySelector("#form");

form.addEventListener("submit", function(evt){
    evt.preventDefault();
    const query = form.elements.query.value;
    fetch("/palette", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        body: new URLSearchParams ({
            query: query,

        })
    })
    .then((response) => response.json())
    .then(data => {
        const colors = data.colors;
        const container = document.querySelector(".container");
        container.innerHTML = "";
        for(const color of colors){
            const div = document.createElement("div");
            div.classList.add("color");
            div.style.backgroundColor = color;
            div.style.width = `calc(100%/ ${colors.length})`

            div.addEventListener("click", function () {
                navigator.clipboard.writeText(color);
            })

            const span = document.createElement("span");
            span.innerHTML = color
            div.appendChild(span);
            container.appendChild(div)
        }
    })
})