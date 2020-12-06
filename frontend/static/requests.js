const get_data = async () => {
    return await axios.get("/api/offers")
        .then((result) => result.data);
}

const render_offers = (offers) => {
    document.getElementById('offers-list').innerHTML = offers.map(({id, name, price}) =>
                `<div class="good">
                  <a href="/offer/${id}"><img src="picshite.png" style="width: 100%;">
                  <p class="name">${name}</p></a>
                  <p class="price">${parseFloat(price).toFixed(2)}</p>
                </div>`
            ).join('');
}

const render_offer_info = (offer) => {
    document.getElementById('offer-info-container').innerHTML = `<div style="display: grid; grid-template-columns: 1fr 2fr">
                <div style="grid-column: 1; grid-row: 1"><a href="/"><p style="color: #5e72e4">Back</p></a></div>
                <div style="grid-column: 1; grid-row: 2"><img src="../../pics/white.png" style=" height: 200px"></div>
                <div style="grid-column: 2; grid-row: 2">
                  <p>Name: ${offer.name}</p>
                  <p>Category: ${offer.category}</p>
                  <p>Count: ${offer.count}</p>
                  <p>Release Date: ${offer.release_date}</p>
                  <p>Price: ${parseFloat(offer.price).toFixed(2)}</p>
                 <input type="button" name="Buy" value="Buy!" style="width: 100px">
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