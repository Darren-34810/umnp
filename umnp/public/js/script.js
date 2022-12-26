var dropdown = document.querySelector("#dropdown")

function open_dropdown() {
    dropdown.classList.remove('hidden')
    document.body.style.height = '100vh'
    document.body.style.overflowY = 'hidden'
}

function close_dropdown() {
    dropdown.classList.add('hidden')
    document.body.style.height = 'unset'
    document.body.style.overflowY = 'unset'
}

dropdown.addEventListener('click', close_dropdown)
