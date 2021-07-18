const BASE_URL = "http://localhost:5000/api"

//generate HTML

function cupcakeHTML(cupcake) {
    return `
        <div data-cupcake-id=${cupcake.id}>
            <li>
                ${cupcake.flavor}  ${cupcake.size}  ${cupcake.rating}
                <button class='delete'>X</button>
            </li>
            <img class='img' src='${cupcake.image}'>
        </div>
    `   
}

//Cupcake List
async function cupcakeList() {
    const resp = await axios.get(`${BASE_URL}/cupcakes`)

    for(let cupcakeData of resp.data.cupcakes) {
        let newCupcake = $(cupcakeHTML(cupcakeData))
        $('#list').append(newCupcake)
    }
}

//Adding a new cupcake using form
$('#cupcake-form').on('submit', async function(e) {
    e.preventDefault()

    let flavor = $('#flavor').val()
    let rating = $('#rating').val()
    let size = $('#size').val()
    let image = $('#image').val()

    const newCupcakePost = await axios.post(`${BASE_URL}/cupcakes`, {flavor, rating, size, image})
    let newCupcake = $(cupcakeHTML(newCupcakePost.data.cupcake))
    $('#list').append(newCupcake)
    $('#cupcake-form').trigger('reset')
})


//Deleting a cupcake
$("#list").on("click", ".delete", async function (e) {
    e.preventDefault();
    let $cupcake = $(e.target).closest("div");
    let cupcakeId = $cupcake.attr("data-cupcake-id");
  
    await axios.delete(`${BASE_URL}/cupcakes/${cupcakeId}`);
    $cupcake.remove();
  });
  
  
  $(cupcakeList);




