const smallSections = document.querySelectorAll('.section--small')
const largeSections = document.querySelectorAll('.section--large')
const obsOptSmall = {
root: null,
threshold: 0.25
}

const obsOptLarge = {
root: null,
threshold: 0.1
}

function showSection(entries, observer) {
    const [entry] = entries
    if(entry.isIntersecting) {
    entry.target.classList.remove('section--hidden')
    observer.unobserve(entry.target)}
}

const obsSmall = new IntersectionObserver(showSection, obsOptSmall)

smallSections.forEach( value => {
    obsSmall.observe(value)
}
)
const obsLarge = new IntersectionObserver(showSection, obsOptLarge)
largeSections.forEach(value => {
    obsLarge.observe(value)
})