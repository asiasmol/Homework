const buttonSeason1 = document.querySelector('.button-1')
const buttonSeason2 = document.querySelector('.button-2')
const buttonSeason3 = document.querySelector('.button-3')
const tableSeasons = document.querySelector('.table-seasons')
const closeButton = document.querySelector(".close-button")

function sendSeasonInfo(season){
    fetch(`${window.origin}/api/penguins?season=${season}`, {
    // method: "GET", domyślnie get
    // credentials: "include",
    cache: "no-cache",
    headers: new Headers({
      "content-type": "application/json"
    })
  })
  .then((response) => response.json())
  .then(response => {
      makeTable(response)
  })
}

function makeTable(episodes){
    episodes.forEach((episode) => {
        const htmlTemplate = `
            <tr>
                <td>${episode['title']}</td>
                <td>${episode['overview']}</td>
            </tr>
            `
            tableSeasons.innerHTML += htmlTemplate
    })

}

function clearTable() {
    htmlClear = ''
    tableSeasons.innerHTML = htmlClear
}


buttonSeason1.addEventListener('click', () =>{
    console.log(buttonSeason1.textContent)
    sendSeasonInfo(buttonSeason1.textContent)
    // get_title_season(buttonSeason1.textContent)
})
buttonSeason2.addEventListener('click', () => {
    console.log(buttonSeason2.textContent)
    sendSeasonInfo(buttonSeason2.textContent)
    // get_title_season(buttonSeason2.textContent)
})
buttonSeason3.addEventListener('click', () => {
    console.log(buttonSeason3.textContent)
    sendSeasonInfo(buttonSeason3.textContent)
    // get_title_season(buttonSeason3.textContent)
})
closeButton.addEventListener("click", clearTable)

// function get_title_season(season){
//     fetch(`/api/penguins/${JSON.stringify(season)}`)
//
// }