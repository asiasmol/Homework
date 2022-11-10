const spaceForMovie = document.querySelector("#movie")
const actors = document.querySelectorAll('.actors-modal')
const closeButton = document.querySelector(".close-button")

function getData(name) {
    return fetch(`/api/actors/movie?actorName=${name}`, {
            headers: new Headers({
                "content-type": "application/json",
                'Accept': 'application/json'
            })
        })
        .then((response) => response.json())
}

function getTemplate(movie) {
    const htmlTemplate = `<p>${movie}</p>`
    spaceForMovie.innerHTML += htmlTemplate
}

function getActorName() {
    const actorsName = [...actors]
    actorsName.forEach(actor => actor.addEventListener('click', () => {
        let actorName = actor.textContent
        $('#actorsMovie').modal('show')
        getData(actorName).then(data => {
            getTemplate(data['title'])
        })
    }))
}

function clearTable() {
    htmlClear = ''
    spaceForMovie.innerHTML = htmlClear
}

closeButton.addEventListener('click', clearTable)

getActorName()