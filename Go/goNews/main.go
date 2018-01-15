package main

import (
	"fmt"

	"./src/feedManage"
)

func main() {
	feedInfo, err := feedManage.NewFeedInfo("db.json")
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Printf("%v\n", feedInfo)

	newFeeds := feedManage.NewFeedContent(feedInfo.Subscription)

	err = feedManage.GenFeedJSONResult("result.json", newFeeds)
	if err != nil {
		fmt.Println(err)
		return
	}

	fmt.Println("Complete")
}
