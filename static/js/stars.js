let buttonShowStars = document.querySelector('#show-actors')
let spaceForListStars = document.querySelector('.list-stars')
let spaceForMovie = document.querySelector('#movies')


function getStars() {
    return fetch(`/api/stars/`, {
        headers: new Headers({
            "content-type": "application/json",
            'Accept': 'application/json'
        })
    })
        .then((response) => response.json())
}

buttonShowStars.addEventListener('click', () => {
    getStars().then(data => {
        getTable(data)
    }).then(() => getActorName())
})

function getTable(stars) {
    let arrayStars = [...stars]
    arrayStars.forEach(star => {
        const htmlTemplate = `<tr>
                                <td class="actors-movie">${star['name']}</td>
                                <td>${star['birthday']}</td>
                                <td>${star['count']}</td>
                            </tr>`
        spaceForListStars.innerHTML += htmlTemplate
    })
}

function getMovie(name) {

    return fetch(`/api/movie/star?actorsName=${name}`, {

        headers: new Headers({
            "content-type": "application/json",
            'Accept': 'application/json'
        })
    })
        .then((response) => response.json())
}

function getActorName() {
    let actors = document.querySelectorAll('.actors-movie')
    const actorsName = [...actors]
    actorsName.forEach(actor => actor.addEventListener('click', () => {
        spaceForMovie.innerHTML = ''
        let actorName = actor.textContent
        $('#actorsMovies').modal('show')
        getMovie(actorName).then(data => {
            console.log(data['title'])
            getTemplate(data['title'])
        })
    }))
}

function getTemplate(movie) {
    const htmlTemplate = `<p>${movie}</p>`
    spaceForMovie.innerHTML += htmlTemplate
}



