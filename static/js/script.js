const smallSections = document.querySelectorAll('.section--small')
const largeSections = document.querySelectorAll('.section--large')
const nav = document.querySelector('.navbar')
const title = document.querySelector('#title')


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

function stickyNav(entries, observer) {
    if(!entries[0].isIntersecting) {
    nav.classList.add('sticky')
    } else {
    nav.classList.remove('sticky')
    }


}

const navObsOpts = {
    root: null,
    threshold: 0.1,
    rootMargin: `-${nav.getBoundingClientRect().height}px`

}

const navObs = new IntersectionObserver(stickyNav, navObsOpts)
navObs.observe(title)