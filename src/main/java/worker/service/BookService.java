package worker.service;

import worker.bean.Book;

import java.util.List;


public interface BookService{


    int deleteByPrimaryKey(Integer id);

    int insert(Book record);

    Book selectByPrimaryKey(Integer id);

    int updateByPrimaryKey(Book record);

    List<Book>  selectAll();

}
