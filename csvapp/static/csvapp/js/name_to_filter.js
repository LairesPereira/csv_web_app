function name_to_filter() {
    fetch("name_to_filter/?description_filter=" + document.getElementById('name_to_filter_input').value.toLowerCase())
    .then((response) => response.json())
    .then((data) => {
        document.getElementById('filtered_table_title').innerHTML = 
        'Transações realizadas para: ' + document.getElementById('name_to_filter_input').value
        
        document.getElementById('table-continer-2').innerHTML = data.filtered_table
    })
}