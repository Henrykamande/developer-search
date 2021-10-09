// get search form and page link
let searchForm= document.getElementById("searchForm")
let pageLinks= document.getElementsByClassName("page-link")

// ensure search form exist
if(searchForm){
    for (let i=0; pageLinks.length> i; i++){
        pageLinks[i].addEventListener('click', function (e) {
            e.preventDefault()
            //geting data attribute
            let page = this.dataset.page
            // Add hidden search input to form
            searchForm.innerHTML += `<input value=${page} name='page' hidden />`
            //submit form
            console.log(searchForm.innerHTML)
            searchForm.submit()

        })
    }

}

