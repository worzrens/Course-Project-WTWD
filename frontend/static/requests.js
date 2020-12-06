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