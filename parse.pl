
open(FILE, "courses.txt") or die "file not found";
my @lines = <FILE>;
my $content = join('', @lines);

my @courses = ();

foreach $line (@lines) {
	if( $line =~ /([A-Z]{4}.[0-9]{4}-[A-Z]{1,2}[0-9]{1,2})/)
	{
		push @courses, $1;
	}
}
print @courses;
