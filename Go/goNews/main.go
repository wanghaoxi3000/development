package main

import (
	"fmt"
	"time"

	"./src/feedManage"
)

func main() {
	feedInfo, err := feedManage.NewFeedInfo("db.json")
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Printf("%v\n", feedInfo)

	flushNum := 1
	for {
		newFeeds := feedManage.NewFeedContent(feedInfo.Subscription)
		err = feedManage.GenFeedJSONResult("result.json", newFeeds)
		if err != nil {
			fmt.Println(err)
			return
		}

		fmt.Printf("第 %d 次刷新数据完成, 时间: %s \n", flushNum, time.Now().Format("2006-01-02 15:04:05"))
		flushNum++
		time.Sleep(time.Duration(feedInfo.FlushTime) * time.Second)
	}
}
