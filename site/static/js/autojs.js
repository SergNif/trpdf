$(document).ready(function() {
    let debounce;
    $('.search-box').on('keydown', function (e) { 
      clearTimeout(debounce)
      debounce = setTimeout(() => {
              getAutoComplete();  
      }, 300);
    })
  })

  function getAutoComplete() {
          const term = $('.search-box').val();
          fetch(`http://localhost:8080/autocomplete?term=${encodeURIComponent(term.trim())}`)
        //     .then((resp) => resp.json())
        //     .then((data) => {
        //             $('.results').empty();
        //             for (let i = 0; i < data.length; i++) {
        //                     $('.results').append(`<li>${data[i]}</li>`)
        //             }
        //           })
        // ws.onmessage = function(event) {
                var messages = document.getElementById('autocomplete');
                var message = document.createElement('li');
                // var content = document.createTextNode(event.data);
                // message.appendChild(content);
                messages.appendChild(message);
        //     };
  }