function load_slider() {
    from_distance = document.getElementById('from_distance_slider');
    to_distance = document.getElementById('to_distance_slider');
    from_day = document.getElementById('from_days_slider');
    to_day = document.getElementById('to_days_slider');
    distance_label = document.getElementById('distance_label');
    days_label = document.getElementById('days_label');

    change_value();
    from_distance.oninput = function() {
        change_value();
    }
    to_distance.oninput = function() {
        change_value();
    }
    from_day.oninput = function() {
        change_value();
    }
    to_day.oninput = function() {
        change_value();
    }
}

function change_value() {
    // Distance
    if (from_distance.value == to_distance.value &&
        (from_distance.value == 0 || from_distance.value == from_distance.max)) {
            distance_label.innerHTML = 'Wszystkie';
    } else if (from_distance.value == to_distance.value) {
        distance_label.innerHTML = 'Rowne ' + from_distance.value + ' km';
    } else if (parseInt(from_distance.value) > parseInt(to_distance.value)) {
        distance_label.innerHTML = 'Od ' + from_distance.value + ' km';
    } else {
        distance_label.innerHTML = 'Od ' + from_distance.value + ' do ' + to_distance.value + ' km';
    }

    if (from_day.value == to_day.value &&
        (from_day.value == 0 || from_day.value == from_day.max)) {
            days_label.innerHTML = 'Wszystkie';
    }
    else if (from_day.value == to_day.value) {
        days_label.innerHTML = 'Rowne ' + from_day.value + ' dni temu';
    } else if (parseInt(from_day.value) > parseInt(to_day.value)) {
        days_label.innerHTML = from_day.value + ' i wiecej dni temu';
    } else {
        days_label.innerHTML = 'Od ' + from_day.value + ' do ' + to_day.value + ' dni';
    }
    save_cookie();
}