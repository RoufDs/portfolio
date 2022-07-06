var myIndex = 0;
carousel();

function carousel() {
    var i;
    var x = document.getElementsByClassName("myslides");
    for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";  
    }
    myIndex++;
    if (myIndex > x.length) {myIndex = 1}    
    x[myIndex-1].style.display = "block";  
    setTimeout(carousel, 9000);
}

const url = window.location.href
const myInput = document.getElementById("my_input")
const myResults = document.getElementById("my_results")

const csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value

const sendSearchData = (my_input) => {
    $.ajax({
        type: "POST",
        url: "search/",
        data: {
            "csrfmiddlewaretoken": csrf,
            "my_input": my_input
        },
        success: (res) => {
            const data = res.data
            if (Array.isArray(data)) {
                data.forEach((my_input) => {
                    myResults.innerHTML = `
                        <a href="${my_input.url}" class="search-details">
                            <div class="search-details-image">
                                <img src="${my_input.image}"/>                           
                            </div>
                            <div class="search-details-name">
                                <h2>${my_input.name}</h2>
                            </div>
                        </a>
                    `
                })
            } else {
                if (myInput.value.length > 0) {
                    myResults.innerHTML = `<b>${data}</b>`
                } else {
                    myResults.classList.add("not-visible")
                }
            }
        }
    })
}

myInput.addEventListener("keyup", (e) => {
    console.log(e.target.value);

    if (myResults.classList.contains("not-visible")) {
        myResults.classList.remove("not-visible")
    }

    sendSearchData(e.target.value)
})