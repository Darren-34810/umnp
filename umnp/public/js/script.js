// Navbar Dropdown
var dropdown = document.querySelector('#dropdown')

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
// End of Navbar Dropdown

// Contact Form Mailto
var destinationEmails = {
    'business': 'inquiry@umnpictures.com',
    'career': 'career@umnpictures.com',
    'intern': 'intern@umnpictures.com',
}

var contactForm = document.querySelector('#contact_form')

function redirectMail(e) {
    e.preventDefault()
    var name = document.querySelector('#name').value
    var inquiry = document.querySelector('#inquiry').value
    var email = document.querySelector('#email').value
    var phone = document.querySelector('#phone').value
    var message = document.querySelector('#message').value

    var subject = `${name} (${email} // ${phone})`
    var destinationEmail = destinationEmails[inquiry]

    var mailto = document.createElement('a')
    var hrefString = `mailto:${destinationEmail}?`
    hrefString += `subject=${subject}&`
    hrefString += `body=${message}`
    mailto.href = hrefString
    mailto.click()
}

contactForm?.addEventListener('submit', redirectMail)
// End of Contact Form Mailto
