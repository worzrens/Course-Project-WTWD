const get_data = async () => {
    return await axios.get("/api/offers")
        .then((result) => result.data);
}

const get_photo = (type) => {
    const photos = {
        tech: ['https://i.imgur.com/on8KhJA.png', 'https://i.imgur.com/xgjGQtn.jpg', 'https://i.imgur.com/IlKfgTA.jpg', 'https://i.imgur.com/vs4KbGX.jpg'],
        cloth: ['https://i.imgur.com/s8ZgAfW.jpg'],
        home: ['https://i.imgur.com/yCEckl6.jpg'],
    }[type];

    console.log("PHOTOS", photos, type)
    return  photos[Math.floor(Math.random() * photos.length)];
}

const render_offers = (offers, type) => {

    document.getElementById('offers-list').innerHTML = offers.map(({id, name, price}) =>
                `<div class="good">
                  <a href="/offer/${id}"><img src="${get_photo(type)}" style="width: 100%;">
                  <p class="name">${name}</p></a>
                  <p class="price">${parseFloat(price).toFixed(2)}</p>
                </div>`
            ).join('');
}

const buy_item = () => {
    const old_count = document.getElementById('offer-count').textContent;
    const new_count = parseInt(old_count) - 1;
    document.getElementById('offer-count').innerText = new_count.toString();
}

const raise_bet = () => {
    const old_bet = document.getElementById('offer-bet').textContent;
    const new_bet = parseInt(old_bet) + 5;
    document.getElementById('offer-bet').innerText = new_bet.toString();
}

const render_offer_info = (offer) => {
    document.getElementById('offer-info-container').innerHTML = `<div style="height: 100%;">
                <div style="grid-column: 1; grid-row: 1"><a href="/"><p style="color: #5e72e4">Back</p></a></div>
                <div style="grid-column: 1; grid-row: 2"><img src="{% static '/pics/white.png' %}" style="height: 200px;"></div>
                <div style="grid-column: 2; grid-row: 2">
                  <p>Name: ${offer.name}</p>
                  <p>Category: ${offer.category}</p>
                  <p>Count: <span id="offer-count">${offer.count}</span></p>
                  <p>Release Date: ${offer.release_date}</p>
                  <p>Price: ${parseFloat(offer.price).toFixed(2)}</p>
                 <input type="button" name="Buy" value="Buy!" onclick="buy_item()" style="width: 100px">
                </div>
             </div>`;
}

const get_offer_info = async (id) => {
    return await axios.get("/api/offers/"+id)
        .then((result) => result.data);
}

const handleSearch = async (name_query) => {
    return await axios.get('/api/offers-search/', {
        params: {name: name_query}
    }).then((result) => result.data)
}

const handleSearchInput = async (event) => {
    if (event.keyCode === 13) {
        event.preventDefault();
        await handleSearch(event.target.value)
            .then(offers => {
                render_offers(offers)
            })
  }
}