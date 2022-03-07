let get_random_data;

function getRandomPerson() {

    let url = '/api/full';

    fetch(url)
    .then(res => res.json())
    .then((data) => {
        updateScreenValues(
            data.name,
            data.age,
            data.birthday,
            data.cpf,
            data.rg,
            data.cnpj,
            data.address,
            data.state,
            data.state_abbreviation,
            data.city,
            data.bairro,
            data.logradouro
            
        )
    })
    .catch(error => { throw error });
    
}

function updateScreenValues(name, age, birthday, cpf, rg, cnpj, address, state, state_abbreviation, city, bairro, logradouro ) {

    document.getElementById("person-container").innerHTML = ""

    let html = ""

    html += `<strong>Name:</strong> ${name}<br>`
    html += `<strong>Age:</strong> ${age}<br>`
    html += `<strong>Birthday:</strong> ${birthday}<br>`
    html += `<strong>RG:</strong> ${rg}<br>`
    html += `<strong>CPF:</strong> ${cpf}<br>`
    html += `<strong>CNPJ:</strong> ${cnpj}<br>`
    html += `<strong>Address:</strong> ${address}<br>`
    html += `<strong>State:</strong> ${state}<br>`
    html += `<strong>State Abbreviation:</strong> ${state_abbreviation}<br>`
    html += `<strong>City:</strong> ${city}<br>`
    html += `<strong>Bairro:</strong> ${bairro}<br>`
    html += `<strong>Logradouro:</strong> ${logradouro}<br>`
    html += `<br><strong>Github repository</strong> <a href="https://github.com/darkmathew/mkfbr-api">https://github.com/darkmathew/mkfbr-api</a>`

    document.getElementById("person-container").innerHTML = html

}

(function() {
    getRandomPerson();
    setInterval(getRandomPerson, 8000)
})();