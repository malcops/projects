package main

import (
	"container/ring"
	"fmt"
)

// Calculations for golf handicapping according to USGA rules
// https://www.usga.org/handicapping/roh/2020-rules-of-handicapping.html

type golfcourse struct {
    name string
    rating float64
    slope int
    tees string
    par int
    yardage int
}

type score struct {
    date string
    course golfcourse
    score int
}

type scoringrecord struct {
    scores *ring.Ring
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

    scores := scoringrecord{}
    scores.scores = ring.New(20)
}