#!/usr/local/bin/perl

my %map;
create_mapping();
get_necessary_en_doc();

print "PARTY TIME\n";	

sub create_mapping {
	print "PREPARE FOR INVANSION\n";

	open (IN, "../lang_links/idwiki-20170201-enlinks");

	my $line;
	while ($line = <IN>) {
		chop($line);

		my @tokens =  split(/\,/, $line);

		my $title = $tokens[2];
		$title =~ s/\'//g;

		if (length $title > 0) {
			if ($map{$title}){
				$map{$title} = ",$tokens[0]";				
			}else {
				$map{$title} = $tokens[0];
			}
		}

	}

	close(IN);

	print "GET READY\n";
}

sub get_necessary_en_doc {
	print "HERE COMES THE ZOMBIE ATTACK\n";

	open (IN, "tmp-enwiki-20170220-page");
	open (OUT, ">en_id_title_result");

	print OUT "id_en/id_id/title_en\n";

	my $line = <IN>;
	while ($line = <IN>) {
		chop($line);

		my @tokens =  split(/###/, $line);

		my $title = $tokens[1];
		$title =~ s/\_/\s/g;
		$title =~ s/\'//g;

		if (length $title > 0) {
			if ($map{$title}) {

				# print "found! ";
				if ($map{$title} =~ /\,/) {
					my @idss = split(/\,/, $map{$title});
					for my $id (@idss) {
						if (length $id > 0) {
							print OUT "$tokens[0]/$id/$title\n";						
						}
					} 
				} else {
					print OUT "$tokens[0]/$map{$title}/$title\n";
				}
			}			
		}
	}

	close(IN);
	close(OUT);

	print "HUMANS WIN\n";
}