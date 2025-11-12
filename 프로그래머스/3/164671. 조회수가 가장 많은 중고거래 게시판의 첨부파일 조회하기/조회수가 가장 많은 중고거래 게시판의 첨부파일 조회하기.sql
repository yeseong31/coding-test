select concat("/home/grep/src/", a.board_id, "/", b.file_id, b.file_name, b.file_ext) file_path
from used_goods_board a join used_goods_file b on a.board_id = b.board_id
where views = (select max(views) from used_goods_board)
order by b.file_id desc;