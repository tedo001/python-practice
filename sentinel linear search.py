<script>
// javascript implementation of the approach    
// Function to search x in the given array
    function sentinelSearch(arr , n , key) {

        // Last element of the array
        var last = arr[n - 1];

        // Element to be searched is
        // placed at the last index
        arr[n - 1] = key;
        var i = 0;

        while (arr[i] != key)
            i++;

        // Put the last element back
        arr[n - 1] = last;

        if ((i < n - 1) || (arr[n - 1] == key))
            document.write(key + " is present at index " + i);
        else
            document.write("Element Not found");
    }

    // Driver code
    
        var arr = [ 10, 20, 180, 30, 60, 50, 110, 100, 70 ];
        var n = arr.length;
        var key = 180;

        sentinelSearch(arr, n, key);

// This code is contributed by todaysgaurav 
</script>
