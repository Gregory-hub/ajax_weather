let responseCity = document.querySelector('.city')
let responseTemperature = document.querySelector('.temperature')

document.forms.city_form.onsubmit = function(e){
    e.preventDefault()

    var input = document.forms.city_form.request_city.value
    input_text = input
    input = encodeURIComponent(input)
    console.log("\nRequest data:", input)
    if(input !== ''){
        var xhr = new XMLHttpRequest()
        xhr.open('GET', 'http://localhost:8000/ajax?' + 'request_city=' + input)

        xhr.onreadystatechange = function(){
            if(xhr.readyState === 4 && xhr.status === 200){
                response = JSON.parse(xhr.response)

                let city = response['city']
                let temperature = response['temperature']

                if(city !== null){
                    responseCity.style = 'border-top: 1px solid black; border-bottom: 1px solid black;'
                    responseTemperature.style = 'border-top: 1px solid black; border-bottom: 1px solid black;'

                    responseCity.innerText = responseCity.textContent = 'City: ' + city
                    responseTemperature.innerText = responseTemperature.textContent = 'Temperature: ' + temperature
                } else {
                    responseCity.style = 'border-top: 1px solid black; border-bottom: 1px solid black;'
                    responseTemperature.style = ''
                    responseCity.innerText = responseCity.textContent = "Server can't find " + input_text
                    responseTemperature.innerText = responseTemperature.textContent = ''

                }
            }
        }

        xhr.send()
    }
}
