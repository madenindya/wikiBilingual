#!/usr/local/bin/perl

open (IN, "idwiki-20170201-langlinks.sql");
open (OUT, ">idwiki-20170201-enlinks");

my $line;
while ($line = <IN>) {
	chop($line);

	# detect if there's english article
	if ($line =~ /\,\'en\'\,/) {

		$line =~ s/INSERT INTO .* VALUES //;
		$line =~ s/;$//;

		my @tokens = split(/\)\,\(/, $line);

		for my $token (@tokens) {
			$token =~ s/^\(//;
			$token =~ s/\)$//;
			if ($token =~ /\,\'en\'\,/) {
				print OUT "$token\n";
			}
		}

	}
}

close(IN);
close(OUT);