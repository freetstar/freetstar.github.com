#!/bin/bash
    sed -i  's/^[>]//' *
#sed -i  's#www.freetstar.com/index.php#www.freetstar.com#g' *
    sed -i  's/^[[:space:]]*//' *
    sed -i  '/^[a-z]/s/^.*/    &/g' *
