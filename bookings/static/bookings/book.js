document.addEventListener('DOMContentLoaded', function () {
    load_cart()
    load_services()

    let cartTable = document.querySelector('#cart-table');
    let cartButton = document.querySelector('#showcart');
    cartButton.onclick = function () {
        if (cartTable.classList.contains('show')) {
            cartTable.classList.remove("show")
        } else {
            cartTable.classList.add("show")
        }
    }

    let step1 = document.querySelector('#step1');
    let step2 = document.querySelector('#step2');
    let step3 = document.querySelector('#step3');
    step2.classList.add("hide");
    step3.classList.add("hide");


    let proceedButton = document.querySelector('#proceed');
    proceedButton.onclick = function () {
        if (!cart.length) {
            alert('You did not choose any services.')
        } else {
            // hide step 1 tab
            step1.classList.add("hide")
            // display step 2
            step2.classList.remove("hide")
            // change highlight in nav
        }
    }

});

// 1. STEP 1 - choose services

let cart = []

async function fetch_services() {
    // load services from the server
    const response = await fetch(`services`);
    const services = await response.json();
    return services;
}

async function load_services() {
    let services = await fetch_services()


    // prepare a table with services
    let inner =
        `
    <tr>
    <th>ID</th>
    <th>Name</th>
    <th>Description</th>
    <th>Duration</th>
    <th>Price</th>
    <th></th>
    </tr>
    `

    services.forEach(service => {

        button = `<td><button class="add btn btn-primary btn-sm" data-id=${service.id}>Add</button></td>`

        inner +=
            `
    <tr data-id=${service.id}">
    <td>${service.id}</td>
    <td>${service.name}</td>
    <td>${service.description}</td>
    <td>${service.duration}</td>
    <td>${service.price}</td>
    ${button}
    </tr>
    `
    })

    // append the table to the page
    let table = document.createElement('table')
    table.classList.add('table', 'mt-3');
    table.innerHTML = inner;

    let anchor = document.querySelector('#services-table')
    anchor.appendChild(table);

    // add listeners for add to cart buttons
    const buttons = document.querySelectorAll('.add');
    buttons.forEach(element => element.onclick = function (e) {
        add(e, services)
    });
}

function load_cart() {
    let anchor = document.querySelector('#cart-table')
    anchor.innerHTML = '';
    let inner =
        `
    <tr>
    <th>ID</th>
    <th>Name</th>
    <th>Description</th>
    <th>Duration</th>
    <th>Price</th>
    <th></th>
    </tr>
    `;

    if (!cart.length) {
        inner +=
            `
            <tr>
            <td colspan="6">Cart is empty</td>
            </tr>
            `;
    } else {
        // prepare a table with services
        cart.forEach(service => {

            button = `<td><button class="remove btn btn-danger btn-sm" data-id=${service.id}>Remove</button></td>`

            inner +=
                `
                <tr data-id=${service.id}">
                <td>${service.id}</td>
                <td>${service.name}</td>
                <td>${service.description}</td>
                <td>${service.duration}</td>
                <td>${service.price}</td>
                ${button}
                </tr>
                `
        })
    }

    // append the table to the page
    let table = document.createElement('table')
    table.classList.add('table', 'mt-3');
    table.innerHTML = inner;

    anchor.appendChild(table);

    // add listeners for add to cart buttons
    const buttons = document.querySelectorAll('.remove');
    buttons.forEach(element => element.onclick = function (e) {
        remove(e)
    });

}

function add(e, services) {
    // convert from caller to service
    const id = e.target.dataset.id;
    let found = services.find(obj => { return obj.id == id });
    console.log(found);
    // add this service to the cart
    cart.push(found);
    console.log(cart);
    // reload cart
    load_cart(cart);

    // change the badge
    let badge = document.querySelector('.badge');
    badge.innerHTML = cart.length
}

function remove(e) {
    // convert from caller to service
    const id = e.target.dataset.id;
    cart = cart.filter(obj => obj.id != id);
    console.log(cart);
    // reload cart
    load_cart(cart);

    let badge = document.querySelector('.badge');
    badge.innerHTML = cart.length
}

// PHASE 2 - choose dates


