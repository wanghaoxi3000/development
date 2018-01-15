package feedManage

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"os"

	"github.com/mmcdole/gofeed"
)

// FeedInfo feed 源数据结构
type FeedInfo struct {
	FlushTime    int
	Subscription []string
}

// FeedContent 每个 feed 源拉取数据的结构
type FeedContent struct {
	Title   string
	Updated string
	Items   []*feedItem
}

// 每个 feed 源子项的数据结构
type feedItem struct {
	Title   string
	Updated string
	Link    string
}

// NewFeedInfo 从指定json读取feed数据源信息
func NewFeedInfo(path string) (*FeedInfo, error) {
	jsonFile, err := os.Open(path)
	defer jsonFile.Close()
	if err != nil {
		return nil, err
	}

	feed := new(FeedInfo)
	buf, _ := ioutil.ReadAll(jsonFile)
	err = json.Unmarshal(buf, feed)
	if err != nil {
		return nil, err
	}

	return feed, nil
}

// NewFeedContent 拉取feed数据
func NewFeedContent(subscription []string) []*FeedContent {
	feeds := make([]*FeedContent, 0)

	for _, v := range subscription {
		ret, err := feedParser(v)
		if err != nil {
			fmt.Println(err)
			continue
		}

		feeds = append(feeds, ret)
	}

	return feeds
}

// GenFeedJSONResult 将拉取的 feed 数据组写入到指定文件中
func GenFeedJSONResult(path string, content []*FeedContent) error {
	b, err := json.Marshal(content)
	if err != nil {
		return err
	}

	var out bytes.Buffer
	json.Indent(&out, b, "", "  ")

	_, err = os.Stat(path)
	if !os.IsNotExist(err) {
		os.Remove(path)
	}

	jsonFile, err := os.Create(path)
	defer jsonFile.Close()
	if err != nil {
		return err
	}

	fileContent, _ := ioutil.ReadAll(&out)
	jsonFile.Write(fileContent)
	return nil
}

func feedParser(url string) (*FeedContent, error) {
	feed := new(FeedContent)
	var item *feedItem
	fp := gofeed.NewParser()

	feedSource, err := fp.ParseURL(url)
	if err != nil {
		return nil, err
	}

	feed.Title = feedSource.Title
	feed.Updated = feedSource.Updated
	feed.Items = make([]*feedItem, 0)
	for i, v := range feedSource.Items {
		item = new(feedItem)

		item.Title = v.Title
		item.Updated = v.Updated
		item.Link = v.Link

		feed.Items = append(feed.Items, item)
		if i == 4 {
			break
		}
	}

	return feed, err
}
