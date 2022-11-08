let name = document.querySelector('.name')
let genre = document.querySelector('.genre')
let table = document.querySelector('.actors-genre')

function getData(name, genre) {
    console.log(name, genre)
    return fetch(`/api/actors?name=${name}&genre=${genre}`, {
        headers: new Headers({
            "content-type": "application/json"
        })
    })
        .then((response) => response.json())
}

function makeTable(data) {
    data.forEach((actor) => {
        const htmlTemplate = `<tr><td>${actor['name']}</td></tr>`
        table.innerHTML += htmlTemplate
    })
}


function downland_data(name, genre) {
    name.addEventListener('input', () => {
        console.log(name.value)
        table.innerHTML = ''
        getData(name.value, genre.value)
            .then(data => {
                makeTable(data)
            })
        genre.addEventListener('change', () => {
            table.innerHTML = ''
            getData(name.value, genre.value)
                .then(data => {
                    makeTable(data)
                })
        })
    })
}


downland_data(name, genre)
getData("", "Action")
    .then(data => {
        makeTable(data)
    })