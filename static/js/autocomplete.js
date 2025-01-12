function binaryRangeSearch(arr, target) {
    let left = 0;
    let right = arr.length - 1;
    let start = -1;
    let end = -1;

    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        if (arr[mid].startsWith(target)) {
            start = mid;
            right = mid - 1;
        } else if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    left = 0;
    right = arr.length - 1;
    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        if (arr[mid].startsWith(target)) {
            end = mid;
            left = mid + 1;
        } else if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    return [start, end];
}
function capitalizeFirstLetter(string) {
    return string.charAt(0).toUpperCase() + string.slice(1);
}
(function($) {
    // jQuery plugin definition
    $.fn.autocomplete = function(input_data, options = {}) {
        const data = input_data.map(item => item.toLowerCase());
        // lower case the input data
      return this.each(function() {
        const $input = $(this);
        const $suggestionsContainer = $('<div class="autocomplete-list"></div>');
        $input.after($suggestionsContainer);
        
        // Optional callback when a suggestion is selected
        const onSelect = options.onSelect || function(item) { console.log('Selected:', item); };

        // Handle input change event
        $input.on('input', function() {
          const query = $input.val().toLowerCase();
          // Filter data based on query, using startsWith and binary search
          const [start, end] = binaryRangeSearch(data, query);
          if (start === -1) {
            $suggestionsContainer.empty().hide();
            return;
          }
          const matches = data.slice(start, end + 1).map(capitalizeFirstLetter);
          $suggestionsContainer.empty().hide();
          
          if (matches.length > 0) {
            matches.forEach(function(item) {
              const $item = $('<div class="autocomplete-item"></div>').text(item);
              $item.on('click', function() {
                $input.val(item);
                $suggestionsContainer.empty().hide();
                onSelect(item);
              });
              $suggestionsContainer.append($item);
            });

            $suggestionsContainer.show();
          }
        });

        // Hide suggestions when clicking outside
        $(document).on('click', function(event) {
          if (!$(event.target).closest($input).length) {
            $suggestionsContainer.empty().hide();
          }
        });
      });
    };
  })(jQuery);
