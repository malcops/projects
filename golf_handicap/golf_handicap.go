package main

import "fmt"

type golfcourse struct {
    name string
    rating float64
    slope int
    tees string
    par int
    yardage int
}

func main(){
    course := golfcourse{}
    // https://course.bluegolf.com/bluegolf/course/course/ospreyvalleyhoot/detailedscorecard.htm
    course.name = "TPC Toronto - Hoot"
    course.rating = 75.4
    course.tees = "gold"
    course.slope = 148
    course.par = 72
    course.yardage = 7134

    fmt.Println(course)
}