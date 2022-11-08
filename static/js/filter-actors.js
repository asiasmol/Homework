let name = document.querySelector('.name')
let genre = document.querySelector('.genre')

async function downland_data(name){
    name.addEventListener('change' yffsadg)
    log_data(name, genre)
}

function log_data(name, genre){
    console.log(name)
    console.log(genre)
}

function getData(name, genre) {
    return fetch(`/api/actors?actorName=${name}?genre=${genre}`, {
            headers: new Headers({
                "content-type": "application/json"
            })
        })
        .then((response) => response.json())
}

downland_data().then(
    log_data()
)

