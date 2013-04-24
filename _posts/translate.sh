#!/bin/bash
    sed -i  's/^[>]//' *
#sed -i  's#www.freetstar.com/index.php#www.freetstar.com#g' *
    sed -i  's/^[[:space:]]*//' 2011*
    sed -i  '/^[a-zA-Z]/s/^.*/    &/g' 2011*
