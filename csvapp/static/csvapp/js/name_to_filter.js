function name_to_filter() {
    input_value = document.getElementById('name_to_filter_input').value.toLowerCase()
    send_checkbox = document.getElementById('send_checkbox').checked
    recived_checkbox = document.getElementById('recived_checkbox').checked

    fetch(`name_to_filter/?description_filter=${input_value}&send_checkbox=${send_checkbox}&recived_checkbox=${recived_checkbox}`)
    .then((response) => response.json())
    .then((data) => {
        document.getElementById('filtered_table_title').innerHTML = 
        'Transações realizadas para: ' + document.getElementById('name_to_filter_input').value
        document.getElementById('table-continer-2').innerHTML = data.filtered_table
    })
}