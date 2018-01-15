package dao

import (
	"github.com/jinzhu/gorm"
	_ "github.com/jinzhu/gorm/dialects/sqlite"
)

func NewSqlitDB(path string) (*gorm.DB, error) {
	db, err := gorm.Open("sqlite3", path)
	return db, err
}
