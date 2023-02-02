function waitForElm(selector) {
    return new Promise(resolve => {
        if (document.querySelector(selector)) {
            return resolve(document.querySelector(selector));
        }

        const observer = new MutationObserver(mutations => {
            if (document.querySelector(selector)) {
                resolve(document.querySelector(selector));
                observer.disconnect();
            }
        });

        observer.observe(document.body, {
            childList: true,
            subtree: true
        });
    });
}

// Eliminates btn-primary class from dropdown (dbc not customizable dropdown button)
waitForElm('#page-selector button').then((elm) => {
    elm.classList.remove('btn-primary');
    let i = document.createElement('i');
    i.classList.add('bi');
    i.classList.add('bi-house');
    i.classList.add('fs-4');
    elm.appendChild(i);
    console.log('hola2');
    console.log('#wsQ8wH!c#52Hz#Fo9Hwk');
});
