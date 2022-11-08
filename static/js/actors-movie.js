const spaceForMovie = document.querySelector("#movie")
const actors = document.querySelectorAll('.actors-modal')
const closeButton = document.querySelector(".close-button")

function getData(name) {
    return fetch(`/api/actors/movie?actorName=${name}`, {
            headers: new Headers({
                "content-type": "application/json"
            })
        })
        .then((response) => response.json())
}

function getMovie(movie) {
    const htmlTemplate = `<p>${movie}</p>`
    spaceForMovie.innerHTML += htmlTemplate
}

function getActorName() {
    const actorsName = [...actors]
    actorsName.forEach(actor => actor.addEventListener('click', async () => {
        let actorName = actor.textContent
        $('#actorsMovie').modal('show')
        getData(actorName).then(data => {
            getMovie(data['title'])
        })
        // const data = await getData(actorName)
        // getMovie(data['title'])
    }))
}

function clearTable() {
    htmlClear = ''
    spaceForMovie.innerHTML = htmlClear
}

closeButton.addEventListener('click', clearTable)

getActorName()